# EMA Hourly Continuation — SLP/USDT P55_200

**Symbol:** SLP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6203 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -3.1548 |
| sortino_ratio | -0.9446 |
| max_drawdown | 0.6811 |
| cagr | -0.3629 |
| net_avg_win | 52.2299 |
| net_avg_loss | -74.9996 |
| avg_hold_time_bars | 18.8311 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
