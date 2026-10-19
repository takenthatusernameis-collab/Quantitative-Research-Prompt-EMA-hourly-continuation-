# EMA Hourly Continuation — BCH/USDT P20_21

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.0816 |
| net_win_rate | 0.2233 |
| gross_profit_factor | 0.4873 |
| gross_win_rate | 0.3243 |
| sharpe_ratio | -20.7676 |
| sortino_ratio | -11.6768 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 3.3761 |
| net_avg_loss | -11.8994 |
| avg_hold_time_bars | 1.7122 |
| exposure | 0.0917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
