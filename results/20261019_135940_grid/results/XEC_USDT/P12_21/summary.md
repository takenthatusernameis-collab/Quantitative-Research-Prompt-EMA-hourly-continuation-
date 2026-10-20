# EMA Hourly Continuation — XEC/USDT P12_21

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1532 |
| net_profit_factor | 0.2824 |
| net_win_rate | 0.3858 |
| gross_profit_factor | 0.9018 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -14.8316 |
| sortino_ratio | -8.3095 |
| max_drawdown | 1.0000 |
| cagr | -0.9870 |
| net_avg_win | 6.6589 |
| net_avg_loss | -14.8090 |
| avg_hold_time_bars | 2.8492 |
| exposure | 0.1975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
