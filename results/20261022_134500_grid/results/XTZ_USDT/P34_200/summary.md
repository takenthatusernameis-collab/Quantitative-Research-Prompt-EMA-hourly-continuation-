# EMA Hourly Continuation — XTZ/USDT P34_200

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.6725 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -2.5434 |
| sortino_ratio | -0.7317 |
| max_drawdown | 0.5921 |
| cagr | -0.2945 |
| net_avg_win | 57.8984 |
| net_avg_loss | -84.4567 |
| avg_hold_time_bars | 26.8230 |
| exposure | 0.5096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
