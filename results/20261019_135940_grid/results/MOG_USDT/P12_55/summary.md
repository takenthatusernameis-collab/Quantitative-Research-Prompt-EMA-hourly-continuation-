# EMA Hourly Continuation — MOG/USDT P12_55

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.7009 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -4.4854 |
| sortino_ratio | -2.0126 |
| max_drawdown | 0.8907 |
| cagr | -0.6158 |
| net_avg_win | 47.6720 |
| net_avg_loss | -60.7792 |
| avg_hold_time_bars | 8.1911 |
| exposure | 0.3771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
