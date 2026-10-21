# EMA Hourly Continuation — XPR/USDT P89_144

**Symbol:** XPR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.7842 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1045 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -1.0175 |
| sortino_ratio | -0.2025 |
| max_drawdown | 0.2265 |
| cagr | -0.0880 |
| net_avg_win | 75.0813 |
| net_avg_loss | -106.3775 |
| avg_hold_time_bars | 10.2789 |
| exposure | 0.0888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
