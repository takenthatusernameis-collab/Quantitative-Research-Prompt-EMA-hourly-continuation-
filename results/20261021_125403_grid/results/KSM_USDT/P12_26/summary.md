# EMA Hourly Continuation — KSM/USDT P12_26

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.5989 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.8825 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -3.6688 |
| sortino_ratio | -1.2454 |
| max_drawdown | 0.7706 |
| cagr | -0.4329 |
| net_avg_win | 42.6183 |
| net_avg_loss | -64.1705 |
| avg_hold_time_bars | 5.5561 |
| exposure | 0.1417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
