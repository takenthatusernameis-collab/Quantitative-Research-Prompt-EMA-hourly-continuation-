# EMA Hourly Continuation — VR/USDT P8_12

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.5277 |
| net_win_rate | 0.4016 |
| gross_profit_factor | 0.7494 |
| gross_win_rate | 0.4057 |
| sharpe_ratio | -3.5965 |
| sortino_ratio | -0.7935 |
| max_drawdown | 0.6217 |
| cagr | -0.3148 |
| net_avg_win | 69.8930 |
| net_avg_loss | -88.9026 |
| avg_hold_time_bars | 7.3811 |
| exposure | 0.0819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
