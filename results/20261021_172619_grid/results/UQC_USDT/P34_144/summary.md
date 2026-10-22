# EMA Hourly Continuation — UQC/USDT P34_144

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.3288 |
| net_win_rate | 0.2810 |
| gross_profit_factor | 0.4149 |
| gross_win_rate | 0.2810 |
| sharpe_ratio | -4.9742 |
| sortino_ratio | -1.0057 |
| max_drawdown | 0.7009 |
| cagr | -0.3803 |
| net_avg_win | 58.1967 |
| net_avg_loss | -69.1572 |
| avg_hold_time_bars | 63.1286 |
| exposure | 0.6000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
