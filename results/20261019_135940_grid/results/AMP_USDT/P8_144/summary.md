# EMA Hourly Continuation — AMP/USDT P8_144

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.3400 |
| net_win_rate | 0.3854 |
| gross_profit_factor | 0.5843 |
| gross_win_rate | 0.3944 |
| sharpe_ratio | -8.4177 |
| sortino_ratio | -3.5310 |
| max_drawdown | 0.9877 |
| cagr | -0.8224 |
| net_avg_win | 14.8199 |
| net_avg_loss | -27.3361 |
| avg_hold_time_bars | 16.7225 |
| exposure | 0.6765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
