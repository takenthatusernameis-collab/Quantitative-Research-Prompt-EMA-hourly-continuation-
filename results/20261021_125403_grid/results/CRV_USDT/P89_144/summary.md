# EMA Hourly Continuation — CRV/USDT P89_144

**Symbol:** CRV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -1.9036 |
| sortino_ratio | -0.4547 |
| max_drawdown | 0.4114 |
| cagr | -0.1878 |
| net_avg_win | 64.1224 |
| net_avg_loss | -85.6930 |
| avg_hold_time_bars | 6.9143 |
| exposure | 0.0880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
