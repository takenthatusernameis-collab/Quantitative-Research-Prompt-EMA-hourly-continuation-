# EMA Hourly Continuation — KAVA/USDT P8_144

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.7315 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.2742 |
| sortino_ratio | -0.6572 |
| max_drawdown | 0.5905 |
| cagr | -0.2703 |
| net_avg_win | 72.3150 |
| net_avg_loss | -93.4155 |
| avg_hold_time_bars | 38.5142 |
| exposure | 0.7423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
