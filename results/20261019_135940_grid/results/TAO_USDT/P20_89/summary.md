# EMA Hourly Continuation — TAO/USDT P20_89

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.7425 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0770 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -3.1531 |
| sortino_ratio | -1.2106 |
| max_drawdown | 0.7788 |
| cagr | -0.4451 |
| net_avg_win | 58.1431 |
| net_avg_loss | -80.6191 |
| avg_hold_time_bars | 10.3735 |
| exposure | 0.3560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
