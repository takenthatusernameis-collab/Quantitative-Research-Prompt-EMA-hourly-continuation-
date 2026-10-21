# EMA Hourly Continuation — TFUEL/USDT P8_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -3.4689 |
| sortino_ratio | -1.3064 |
| max_drawdown | 0.7843 |
| cagr | -0.4511 |
| net_avg_win | 56.1889 |
| net_avg_loss | -67.7461 |
| avg_hold_time_bars | 16.9830 |
| exposure | 0.5426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
