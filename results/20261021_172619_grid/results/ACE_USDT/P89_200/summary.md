# EMA Hourly Continuation — ACE/USDT P89_200

**Symbol:** ACE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7883 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.1037 |
| sortino_ratio | -0.2528 |
| max_drawdown | 0.2922 |
| cagr | -0.1103 |
| net_avg_win | 73.6727 |
| net_avg_loss | -94.1925 |
| avg_hold_time_bars | 18.6265 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
