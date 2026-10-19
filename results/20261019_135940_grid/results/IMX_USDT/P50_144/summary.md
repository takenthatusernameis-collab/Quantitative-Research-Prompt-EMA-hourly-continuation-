# EMA Hourly Continuation — IMX/USDT P50_144

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5892 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -3.3038 |
| sortino_ratio | -1.0388 |
| max_drawdown | 0.7241 |
| cagr | -0.3911 |
| net_avg_win | 42.8468 |
| net_avg_loss | -66.5898 |
| avg_hold_time_bars | 11.9460 |
| exposure | 0.2703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
