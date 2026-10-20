# EMA Hourly Continuation — T/USDT P55_89

**Symbol:** T/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.3971 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.7595 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -6.9985 |
| sortino_ratio | -2.3729 |
| max_drawdown | 0.9526 |
| cagr | -0.6975 |
| net_avg_win | 25.9897 |
| net_avg_loss | -46.3933 |
| avg_hold_time_bars | 6.9880 |
| exposure | 0.1837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
