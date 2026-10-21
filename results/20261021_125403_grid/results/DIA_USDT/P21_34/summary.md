# EMA Hourly Continuation — DIA/USDT P21_34

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6190 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9095 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -3.0954 |
| sortino_ratio | -0.9142 |
| max_drawdown | 0.6715 |
| cagr | -0.3415 |
| net_avg_win | 51.8866 |
| net_avg_loss | -77.0214 |
| avg_hold_time_bars | 5.3075 |
| exposure | 0.1023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
