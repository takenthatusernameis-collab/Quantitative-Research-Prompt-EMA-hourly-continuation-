# EMA Hourly Continuation — QNT/USDT P12_89

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.5456 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -5.9698 |
| sortino_ratio | -2.5437 |
| max_drawdown | 0.9570 |
| cagr | -0.7108 |
| net_avg_win | 27.0673 |
| net_avg_loss | -42.3199 |
| avg_hold_time_bars | 11.1064 |
| exposure | 0.4650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
