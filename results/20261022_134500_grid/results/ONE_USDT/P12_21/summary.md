# EMA Hourly Continuation — ONE/USDT P12_21

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1517 |
| net_profit_factor | 0.2770 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.7056 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -12.7622 |
| sortino_ratio | -7.0590 |
| max_drawdown | 0.9999 |
| cagr | -0.9724 |
| net_avg_win | 6.1900 |
| net_avg_loss | -15.4013 |
| avg_hold_time_bars | 2.1206 |
| exposure | 0.1462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
