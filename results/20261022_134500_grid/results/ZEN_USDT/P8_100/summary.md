# EMA Hourly Continuation — ZEN/USDT P8_100

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.5683 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8497 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -3.7164 |
| sortino_ratio | -1.3064 |
| max_drawdown | 0.8007 |
| cagr | -0.4725 |
| net_avg_win | 35.1896 |
| net_avg_loss | -54.6175 |
| avg_hold_time_bars | 23.9577 |
| exposure | 0.6948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
