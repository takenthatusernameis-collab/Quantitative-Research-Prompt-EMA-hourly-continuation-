# EMA Hourly Continuation — NMR/USDT P34_89

**Symbol:** NMR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9707 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -5.4281 |
| sortino_ratio | -2.0380 |
| max_drawdown | 0.9232 |
| cagr | -0.6318 |
| net_avg_win | 40.3638 |
| net_avg_loss | -58.5163 |
| avg_hold_time_bars | 7.9749 |
| exposure | 0.2603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
