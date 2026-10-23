# EMA Hourly Continuation — XNO/USDT P21_144

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5429 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -5.5665 |
| sortino_ratio | -2.0826 |
| max_drawdown | 0.9155 |
| cagr | -0.6262 |
| net_avg_win | 36.4917 |
| net_avg_loss | -49.9492 |
| avg_hold_time_bars | 14.8670 |
| exposure | 0.4724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
