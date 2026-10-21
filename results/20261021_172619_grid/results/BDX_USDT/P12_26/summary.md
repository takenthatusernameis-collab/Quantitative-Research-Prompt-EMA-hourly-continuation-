# EMA Hourly Continuation — BDX/USDT P12_26

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.3816 |
| net_win_rate | 0.3736 |
| gross_profit_factor | 0.6646 |
| gross_win_rate | 0.3773 |
| sharpe_ratio | -5.1877 |
| sortino_ratio | -1.2333 |
| max_drawdown | 0.7732 |
| cagr | -0.4417 |
| net_avg_win | 46.5059 |
| net_avg_loss | -72.6886 |
| avg_hold_time_bars | 4.3516 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
