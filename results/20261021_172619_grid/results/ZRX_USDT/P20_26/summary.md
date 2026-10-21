# EMA Hourly Continuation — ZRX/USDT P20_26

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.5661 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.2800 |
| sortino_ratio | -0.8656 |
| max_drawdown | 0.6384 |
| cagr | -0.3280 |
| net_avg_win | 51.1695 |
| net_avg_loss | -83.1634 |
| avg_hold_time_bars | 4.9018 |
| exposure | 0.0749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
