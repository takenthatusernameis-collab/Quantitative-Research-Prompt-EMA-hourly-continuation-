# EMA Hourly Continuation — TRAC/USDT P26_89

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.6170 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9377 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.9627 |
| sortino_ratio | -1.4394 |
| max_drawdown | 0.8310 |
| cagr | -0.4981 |
| net_avg_win | 42.0933 |
| net_avg_loss | -61.2216 |
| avg_hold_time_bars | 10.0135 |
| exposure | 0.3031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
