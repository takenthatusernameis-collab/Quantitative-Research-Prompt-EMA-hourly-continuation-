# EMA Hourly Continuation — DCR/USDT P12_55

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9144 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.9659 |
| sortino_ratio | -1.1268 |
| max_drawdown | 0.7464 |
| cagr | -0.4057 |
| net_avg_win | 45.1551 |
| net_avg_loss | -62.0731 |
| avg_hold_time_bars | 10.4242 |
| exposure | 0.3359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
