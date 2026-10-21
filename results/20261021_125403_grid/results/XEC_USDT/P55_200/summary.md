# EMA Hourly Continuation — XEC/USDT P55_200

**Symbol:** XEC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.9018 |
| sortino_ratio | -0.4825 |
| max_drawdown | 0.4744 |
| cagr | -0.1988 |
| net_avg_win | 65.1716 |
| net_avg_loss | -86.3847 |
| avg_hold_time_bars | 25.3208 |
| exposure | 0.3644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
