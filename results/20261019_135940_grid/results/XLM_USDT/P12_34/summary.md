# EMA Hourly Continuation — XLM/USDT P12_34

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1367 |
| net_profit_factor | 0.2331 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.7475 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -10.8429 |
| sortino_ratio | -5.6584 |
| max_drawdown | 0.9993 |
| cagr | -0.9435 |
| net_avg_win | 5.1144 |
| net_avg_loss | -16.8572 |
| avg_hold_time_bars | 3.9327 |
| exposure | 0.2444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
