# EMA Hourly Continuation — TAO/USDT P8_100

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.7683 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.4798 |
| sortino_ratio | -0.9187 |
| max_drawdown | 0.7057 |
| cagr | -0.3535 |
| net_avg_win | 63.9816 |
| net_avg_loss | -84.2510 |
| avg_hold_time_bars | 20.6647 |
| exposure | 0.6444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
