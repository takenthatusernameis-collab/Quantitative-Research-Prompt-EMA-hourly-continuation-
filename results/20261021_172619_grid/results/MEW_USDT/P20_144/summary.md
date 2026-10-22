# EMA Hourly Continuation — MEW/USDT P20_144

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8552 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0081 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -0.9534 |
| sortino_ratio | -0.2735 |
| max_drawdown | 0.3262 |
| cagr | -0.1204 |
| net_avg_win | 80.5594 |
| net_avg_loss | -95.6185 |
| avg_hold_time_bars | 27.7431 |
| exposure | 0.5057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
