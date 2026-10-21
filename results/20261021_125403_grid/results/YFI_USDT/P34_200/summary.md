# EMA Hourly Continuation — YFI/USDT P34_200

**Symbol:** YFI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.8984 |
| sortino_ratio | -0.5005 |
| max_drawdown | 0.4772 |
| cagr | -0.2050 |
| net_avg_win | 70.5806 |
| net_avg_loss | -93.3988 |
| avg_hold_time_bars | 33.5673 |
| exposure | 0.5195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
