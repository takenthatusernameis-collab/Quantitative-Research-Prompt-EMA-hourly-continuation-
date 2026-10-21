# EMA Hourly Continuation — AKT/USDT P8_144

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.9609 |
| net_win_rate | 0.5291 |
| gross_profit_factor | 1.1137 |
| gross_win_rate | 0.5291 |
| sharpe_ratio | -0.1976 |
| sortino_ratio | -0.0566 |
| max_drawdown | 0.1535 |
| cagr | -0.0322 |
| net_avg_win | 92.7888 |
| net_avg_loss | -108.5055 |
| avg_hold_time_bars | 38.5949 |
| exposure | 0.6930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
