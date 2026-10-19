# EMA Hourly Continuation — UNI/USDT P55_200

**Symbol:** UNI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5690 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8417 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.8255 |
| sortino_ratio | -1.0766 |
| max_drawdown | 0.7443 |
| cagr | -0.4123 |
| net_avg_win | 53.7382 |
| net_avg_loss | -75.6408 |
| avg_hold_time_bars | 18.9484 |
| exposure | 0.3505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
