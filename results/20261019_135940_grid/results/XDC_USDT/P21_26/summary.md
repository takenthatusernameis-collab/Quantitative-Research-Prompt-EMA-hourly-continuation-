# EMA Hourly Continuation — XDC/USDT P21_26

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1204 |
| net_profit_factor | 0.0886 |
| net_win_rate | 0.2757 |
| gross_profit_factor | 0.4302 |
| gross_win_rate | 0.3995 |
| sharpe_ratio | -18.5880 |
| sortino_ratio | -9.9971 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 2.9267 |
| net_avg_loss | -12.5822 |
| avg_hold_time_bars | 2.2699 |
| exposure | 0.1242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
