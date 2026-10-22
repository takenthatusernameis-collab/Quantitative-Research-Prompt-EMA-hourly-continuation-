# EMA Hourly Continuation — BOSON/USDT P12_144

**Symbol:** BOSON/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7568 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9977 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -2.5276 |
| sortino_ratio | -0.8569 |
| max_drawdown | 0.6435 |
| cagr | -0.3322 |
| net_avg_win | 71.8455 |
| net_avg_loss | -86.7584 |
| avg_hold_time_bars | 22.8131 |
| exposure | 0.5994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
