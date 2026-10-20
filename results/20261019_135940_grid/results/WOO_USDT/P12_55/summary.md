# EMA Hourly Continuation — WOO/USDT P12_55

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 1.0937 |
| gross_win_rate | 0.4995 |
| sharpe_ratio | -4.4549 |
| sortino_ratio | -1.9365 |
| max_drawdown | 0.9098 |
| cagr | -0.6020 |
| net_avg_win | 47.4564 |
| net_avg_loss | -64.4421 |
| avg_hold_time_bars | 9.3119 |
| exposure | 0.4017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
