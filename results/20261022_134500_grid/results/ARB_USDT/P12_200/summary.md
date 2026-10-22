# EMA Hourly Continuation — ARB/USDT P12_200

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8445 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1042 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.7731 |
| sortino_ratio | -0.1726 |
| max_drawdown | 0.2607 |
| cagr | -0.0802 |
| net_avg_win | 78.5237 |
| net_avg_loss | -104.1119 |
| avg_hold_time_bars | 71.3347 |
| exposure | 0.8041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
