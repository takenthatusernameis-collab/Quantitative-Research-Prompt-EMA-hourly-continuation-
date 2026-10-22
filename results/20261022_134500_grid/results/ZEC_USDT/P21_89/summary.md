# EMA Hourly Continuation — ZEC/USDT P21_89

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.6322 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -3.5683 |
| sortino_ratio | -1.3234 |
| max_drawdown | 0.8010 |
| cagr | -0.4690 |
| net_avg_win | 40.4743 |
| net_avg_loss | -61.1318 |
| avg_hold_time_bars | 11.4075 |
| exposure | 0.3588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
