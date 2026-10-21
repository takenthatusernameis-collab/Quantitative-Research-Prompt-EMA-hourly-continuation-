# EMA Hourly Continuation — ZRX/USDT P89_144

**Symbol:** ZRX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7474 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0628 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -1.7576 |
| sortino_ratio | -0.4596 |
| max_drawdown | 0.4363 |
| cagr | -0.1899 |
| net_avg_win | 71.9040 |
| net_avg_loss | -100.9860 |
| avg_hold_time_bars | 6.8455 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
