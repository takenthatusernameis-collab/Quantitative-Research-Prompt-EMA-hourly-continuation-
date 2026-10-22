# EMA Hourly Continuation — ICP/USDT P34_144

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5976 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -3.7518 |
| sortino_ratio | -1.2097 |
| max_drawdown | 0.7688 |
| cagr | -0.4353 |
| net_avg_win | 46.3783 |
| net_avg_loss | -68.6050 |
| avg_hold_time_bars | 16.7942 |
| exposure | 0.3970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
