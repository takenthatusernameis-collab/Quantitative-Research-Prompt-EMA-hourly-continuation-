# EMA Hourly Continuation — UQC/USDT P8_144

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.3040 |
| net_win_rate | 0.2902 |
| gross_profit_factor | 0.4270 |
| gross_win_rate | 0.2946 |
| sharpe_ratio | -5.3727 |
| sortino_ratio | -1.1227 |
| max_drawdown | 0.7561 |
| cagr | -0.4267 |
| net_avg_win | 50.6832 |
| net_avg_loss | -68.1512 |
| avg_hold_time_bars | 77.5759 |
| exposure | 0.7865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
