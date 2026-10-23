# EMA Hourly Continuation — ONE/USDT P21_89

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6976 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.6843 |
| sortino_ratio | -1.3883 |
| max_drawdown | 0.8249 |
| cagr | -0.4818 |
| net_avg_win | 54.1965 |
| net_avg_loss | -73.0193 |
| avg_hold_time_bars | 12.5592 |
| exposure | 0.4053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
