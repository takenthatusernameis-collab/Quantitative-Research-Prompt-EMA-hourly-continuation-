# EMA Hourly Continuation — RENDER/USDT P55_89

**Symbol:** RENDER/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.5427 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.9220 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -5.7798 |
| sortino_ratio | -2.1321 |
| max_drawdown | 0.9029 |
| cagr | -0.6492 |
| net_avg_win | 39.6935 |
| net_avg_loss | -60.1240 |
| avg_hold_time_bars | 4.0808 |
| exposure | 0.1279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
