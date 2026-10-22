# EMA Hourly Continuation — ZRO/USDT P55_144

**Symbol:** ZRO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6622 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9270 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -2.7190 |
| sortino_ratio | -0.8618 |
| max_drawdown | 0.6298 |
| cagr | -0.3375 |
| net_avg_win | 52.8195 |
| net_avg_loss | -76.1133 |
| avg_hold_time_bars | 9.6013 |
| exposure | 0.2204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
