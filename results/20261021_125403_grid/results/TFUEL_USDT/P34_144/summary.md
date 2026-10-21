# EMA Hourly Continuation — TFUEL/USDT P34_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5888 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.7592 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -3.7935 |
| sortino_ratio | -1.1602 |
| max_drawdown | 0.7436 |
| cagr | -0.4150 |
| net_avg_win | 53.0808 |
| net_avg_loss | -67.0283 |
| avg_hold_time_bars | 16.3156 |
| exposure | 0.3463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
