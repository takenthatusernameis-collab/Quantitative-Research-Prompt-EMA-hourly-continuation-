# EMA Hourly Continuation — TAO/USDT P55_144

**Symbol:** TAO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6605 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.0243 |
| sortino_ratio | -0.9340 |
| max_drawdown | 0.6781 |
| cagr | -0.3632 |
| net_avg_win | 55.1904 |
| net_avg_loss | -80.5293 |
| avg_hold_time_bars | 9.8480 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
