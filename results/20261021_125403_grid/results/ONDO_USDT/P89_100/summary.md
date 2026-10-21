# EMA Hourly Continuation — ONDO/USDT P89_100

**Symbol:** ONDO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 84 |
| net_profit_factor | 0.5965 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8168 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -1.4349 |
| sortino_ratio | -0.1875 |
| max_drawdown | 0.2174 |
| cagr | -0.0821 |
| net_avg_win | 75.2769 |
| net_avg_loss | -104.2416 |
| avg_hold_time_bars | 5.3333 |
| exposure | 0.0204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
