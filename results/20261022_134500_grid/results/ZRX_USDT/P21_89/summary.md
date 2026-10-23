# EMA Hourly Continuation — ZRX/USDT P21_89

**Symbol:** ZRX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -4.4154 |
| sortino_ratio | -1.6263 |
| max_drawdown | 0.8654 |
| cagr | -0.5407 |
| net_avg_win | 44.5298 |
| net_avg_loss | -62.4317 |
| avg_hold_time_bars | 12.5570 |
| exposure | 0.3904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
