# EMA Hourly Continuation — ILV/USDT P55_89

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5203 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -5.5806 |
| sortino_ratio | -2.0320 |
| max_drawdown | 0.9138 |
| cagr | -0.6231 |
| net_avg_win | 33.3722 |
| net_avg_loss | -53.0616 |
| avg_hold_time_bars | 4.2637 |
| exposure | 0.1271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
