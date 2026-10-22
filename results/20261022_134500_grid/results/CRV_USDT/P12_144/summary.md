# EMA Hourly Continuation — CRV/USDT P12_144

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.3855 |
| sortino_ratio | -0.6597 |
| max_drawdown | 0.5529 |
| cagr | -0.2656 |
| net_avg_win | 65.7096 |
| net_avg_loss | -89.2092 |
| avg_hold_time_bars | 43.7816 |
| exposure | 0.7562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
