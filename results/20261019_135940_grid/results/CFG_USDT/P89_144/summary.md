# EMA Hourly Continuation — CFG/USDT P89_144

**Symbol:** CFG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.4591 |
| net_win_rate | 0.4159 |
| gross_profit_factor | 0.6966 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -5.1100 |
| sortino_ratio | -1.6426 |
| max_drawdown | 0.8606 |
| cagr | -0.5420 |
| net_avg_win | 33.9250 |
| net_avg_loss | -52.6048 |
| avg_hold_time_bars | 4.8781 |
| exposure | 0.1146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
