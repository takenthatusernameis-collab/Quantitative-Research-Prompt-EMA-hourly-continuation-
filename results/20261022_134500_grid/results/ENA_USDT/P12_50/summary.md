# EMA Hourly Continuation — ENA/USDT P12_50

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -3.9354 |
| sortino_ratio | -1.7888 |
| max_drawdown | 0.8915 |
| cagr | -0.5725 |
| net_avg_win | 37.7239 |
| net_avg_loss | -52.9646 |
| avg_hold_time_bars | 7.2216 |
| exposure | 0.3407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
