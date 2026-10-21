# EMA Hourly Continuation — TFUEL/USDT P55_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5789 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -3.6846 |
| sortino_ratio | -1.0519 |
| max_drawdown | 0.7119 |
| cagr | -0.3845 |
| net_avg_win | 55.7743 |
| net_avg_loss | -71.9529 |
| avg_hold_time_bars | 12.6536 |
| exposure | 0.2330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
