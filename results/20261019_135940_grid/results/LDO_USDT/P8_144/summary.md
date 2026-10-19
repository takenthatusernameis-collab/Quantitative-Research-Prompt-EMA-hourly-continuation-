# EMA Hourly Continuation — LDO/USDT P8_144

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5631 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7744 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -3.8808 |
| sortino_ratio | -1.1175 |
| max_drawdown | 0.7492 |
| cagr | -0.4235 |
| net_avg_win | 52.1869 |
| net_avg_loss | -69.9850 |
| avg_hold_time_bars | 39.7581 |
| exposure | 0.7771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
